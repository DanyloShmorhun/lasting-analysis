import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from lifelines import CoxPHFitter

def main():
    st.title("Аналіз виживаності за допомогою моделі Кокса")

    # Завантаження обробленого файлу
    file_path = "data/data_for_cox.csv"
    try:
        data = pd.read_csv(file_path)
        if data.columns.duplicated().any():
            st.warning("У файлі є дублікати імен колонок. Вони будуть автоматично перейменовані.")
            data.columns = pd.io.parsers.ParserBase({'names': data.columns})._maybe_dedup_names(data.columns)
        st.success(f"Файл '{file_path}' завантажено автоматично!")
    except FileNotFoundError:
        st.error(f"Файл '{file_path}' не знайдено. Завантажте файл вручну.")
        uploaded_file = st.file_uploader("Завантажте файл 'data_for_cox.csv'", type=["csv"])
        if uploaded_file:
            data = pd.read_csv(uploaded_file)
            if data.columns.duplicated().any():
                st.warning("У файлі є дублікати імен колонок. Вони будуть автоматично перейменовані.")
                data.columns = pd.io.parsers.ParserBase({'names': data.columns})._maybe_dedup_names(data.columns)
            st.write("Перші 5 рядків даних:")
            st.dataframe(data.head())
        else:
            st.stop()

    # Мапінг назв змінних на українську
    covariate_mapping_ukrainian = {
        'temp': 'Температура',
        'sex': 'Стать',
        'dehsev_Mild_dehydration': 'Легке зневоднення',
        'dehsev_Severe_dehydration': 'Важке зневоднення',
        'vomit_avgfrq': 'Середня частота блювоти',
        'antibioticfl': 'Тільки антибіотик',
        'analgesicfl': 'Тільки анальгетик',
        'probioticfl': 'Тільки пробіотик',
        'controlfl': 'Контрольна група'
    }

    # Вибір коваріатів з українськими назвами
    default_covariates = [
        'temp', 'sex', 'dehsev_Mild_dehydration',
        'dehsev_Severe_dehydration', 'vomit_avgfrq',
        'antibioticfl', 'analgesicfl', 'probioticfl', 'controlfl'
    ]
    available_covariates = [cov for cov in default_covariates if cov in data.columns]
    available_covariates_ukrainian = [
        covariate_mapping_ukrainian.get(cov, cov) for cov in available_covariates
    ]

    selected_covariates_ukrainian = st.multiselect(
        "Коваріати:",
        available_covariates_ukrainian,
        default=available_covariates_ukrainian
    )
    selected_covariates = [
        cov for cov in covariate_mapping_ukrainian
        if covariate_mapping_ukrainian[cov] in selected_covariates_ukrainian
    ]

    # Перевірка наявності хоча б одного лікування
    treatment_covariates = ['antibioticfl', 'analgesicfl', 'probioticfl', 'controlfl']
    if not any(cov in selected_covariates for cov in treatment_covariates):
        st.error("Додайте хоча б одну змінну, пов'язану з лікуванням, до коваріатів.")
        st.stop()

        # Вибір колонок для часу і статусу події
    duration_col = "survival_time"  # Колонка для часу виживаності
    event_col = "event_occurred"   # Колонка для статусу події

    # Виведення фіксованих колонок з українським перекладом
    st.write(f"Колонка для часу виживаності: 'Час виживання - днів'")
    st.write(f"Колонка для статусу події: 'Подія відбулася - пацієнт прохворів більше середнього значення'")

    # Словник для перекладу назв колонок на українську
    column_translation = {
        'sex': 'Стать',
        'temp': 'Температура',
        'virusfl': 'Вірусна інфекція',
        'age_years': 'Вік (роки)',
        'dehsev_Mild_dehydration': 'Легке зневоднення',
        'dehsev_Severe_dehydration': 'Важке зневоднення',
        'dehsev_No_dehydration': 'Відсутнє зневоднення',
        'BMI': 'ІМТ (Індекс маси тіла)',
        'vomit_avgfrq': 'Середня частота блювання',
        'antibioticfl': 'Тільки антибіотик',
        'analgesicfl': 'Тільки анальгетик',
        'probioticfl': 'Тільки пробіотик',
        'controlfl': 'Контрольна група'
    }

    # Зворотній словник для отримання оригінальних назв
    reverse_translation = {v: k for k, v in column_translation.items()}

    # Вибір страт (обов'язкова antibioticfl)
    st.subheader("Страти (обов'язково включає 'Тільки антибіотик')")
    use_strata = st.checkbox("Додати додаткові страти?")
    strata = ['antibioticfl']  # Обов'язкова страта
    if use_strata:
        # Відображення колонок українською
        translated_columns = [column_translation.get(col, col) for col in data.columns if col != 'antibioticfl']
        additional_strata_translated = st.multiselect(
            "Виберіть додаткові страти (групування):",
            translated_columns,
            default=[]
        )
        # Конвертація обраних назв назад в оригінальні
        additional_strata = [reverse_translation[col] for col in additional_strata_translated]
        strata.extend(additional_strata)

    # Перевірка: всі страти повинні бути в коваріатах
    if strata:
        missing_in_covariates = [s for s in strata if s not in selected_covariates]
        selected_covariates_original = [reverse_translation.get(col, col) for col in selected_covariates]

        # Перевірка: всі страти повинні бути в оригінальних коваріатах
        missing_in_covariates = [s for s in strata if s not in selected_covariates_original]
        if missing_in_covariates:
            # Переклад відсутніх змінних для виведення повідомлення
            missing_translated = [column_translation.get(col, col) for col in missing_in_covariates]
            st.error(f"Змінні {', '.join(missing_translated)} обрані як страти, але вони відсутні в коваріатах. Додайте їх до списку коваріатів.")
            st.stop()
    # Очищення даних
    selected_columns = selected_covariates + [duration_col, event_col]
    data_selected = data[selected_columns].copy()
    data_selected = data_selected.dropna()  # Видалення рядків із NaN

    # Побудова моделі Кокса
    cox_model = CoxPHFitter(penalizer=0.1)
    cox_model.fit(
        data_selected,
        duration_col=duration_col,
        event_col=event_col,
        strata=strata
    )

    st.subheader("HR та p-value для Лікувань")
    # Фільтрація результатів для лікувальних змінних
    cox_summary = cox_model.summary
    treatment_effects = cox_summary.loc[
        [var for var in treatment_covariates if var in cox_summary.index],
        ['exp(coef)', 'p']
    ].rename(columns={'exp(coef)': 'HR', 'p': 'p-value'})

    treatment_effects = treatment_effects.round(2)
    treatment_effects['Коваріат'] = [
        covariate_mapping_ukrainian.get(var, var) for var in treatment_effects.index
    ]

    st.dataframe(treatment_effects)

    # Графік коефіцієнтів ризику
    st.subheader("Графік коефіцієнтів ризику (Hazard Ratios) для лікування")
    fig, ax = plt.subplots(figsize=(10, 6))
    treatment_effects.set_index('Коваріат')['HR'].plot(kind='barh', ax=ax, color='skyblue')
    plt.axvline(1, color='red', linestyle='--', label='Відсутність ефекту')
    plt.title("Коефіцієнти ризику для груп лікування", fontsize=14)
    plt.xlabel("Коефіцієнт ризику (HR)", fontsize=12)
    plt.ylabel("Групи лікування", fontsize=12)
    plt.legend(fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)

    # Графік p-значень
    st.subheader("Графік рівнів значущості (p-values) для лікування")
    fig, ax = plt.subplots(figsize=(10, 6))
    treatment_effects.set_index('Коваріат')['p-value'].plot(kind='barh', ax=ax, color='salmon')
    plt.axvline(0.05, color='blue', linestyle='--', label='Рівень значущості 0.05')
    plt.title("Рівень значущості (p-значення) для груп лікування", fontsize=14)
    plt.xlabel("p-значення", fontsize=12)
    plt.ylabel("Групи лікування", fontsize=12)
    plt.legend(fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)

    # Висновок
    st.subheader("Висновки:")
    for index, row in treatment_effects.iterrows():
        treatment_name = row['Коваріат']
        hr = row['HR']
        p_value = row['p-value']
        if p_value < 0.05:
            if hr > 1:
                conclusion = f"Лікування '{treatment_name}' збільшує ризик події, а саме, знаходження пацієнта в ліжку більше середнього значення. Не рекомандуємо додавати цей препарат в курс лікування. (HR = {hr:.2f}, p < 0.05)."
            elif hr < 1:
                conclusion = f"Лікування '{treatment_name}' зменшує ризик події, а саме, знаходження пацієнта в ліжку більше середнього значення. Не рекомандуємо додавати цей препарат в курс лікування. (HR = {hr:.2f}, p < 0.05)."
            else:
                conclusion = f"Лікування '{treatment_name}' не змінює ризик події (HR = {hr:.2f}, p < 0.05)."
        else:
            conclusion =  f"Лікування '{treatment_name}' не змінює ризик події, а саме, знаходження пацієнта в ліжку більше середнього значення. Не рекомандуємо додавати цей препарат в курс лікування. (HR = {hr:.2f}, p < 0.05)."
        st.write(conclusion)

if __name__ == "__main__":
    main()
