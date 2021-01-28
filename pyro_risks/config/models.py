ZONE_VAR = "departement"

DATE_VAR = "day"

TARGET = "fires"

PIPELINE_ERA5T_VARS = [
    "strd_min",
    "isi_min",
    "strd_max",
    "d2m_mean",
    "lai_hv_mean",
    "str_mean",
    "ffmc_mean",
    "strd_mean",
    "swvl1_mean",
    "asn_min",
    "fwi_mean",
    "asn_std",
    "ssr_mean",
    "str_max",
    "d2m_min",
    "rsn_std",
    "ssrd_min",
    "isi_mean",
    "ssrd_mean",
    "isi_max",
    "ffmc_max",
    "ffmc_min",
    "ssr_min",
    "str_min",
    "ffmc_std",
]

MODEL_ERA5T_VARS = [
    "str_max",
    "str_mean",
    "ffmc_min",
    "str_min",
    "ffmc_mean",
    "str_mean_lag1",
    "str_max_lag1",
    "str_min_lag1",
    "isi_min",
    "ffmc_min_lag1",
    "isi_mean",
    "ffmc_mean_lag1",
    "ffmc_std",
    "ffmc_max",
    "isi_min_lag1",
    "isi_mean_lag1",
    "ffmc_max_lag1",
    "asn_std",
    "strd_max",
    "ssrd_min",
    "strd_mean",
    "isi_max",
    "strd_min",
    "d2m_min",
    "asn_min",
    "ssr_min",
    "ffmc_min_lag3",
    "ffmc_std_lag1",
    "lai_hv_mean_lag7",
    "str_max_lag3",
    "str_mean_lag3",
    "rsn_std_lag1",
    "fwi_mean",
    "ssr_mean",
    "ssrd_mean",
    "swvl1_mean",
    "rsn_std_lag3",
    "isi_max_lag1",
    "d2m_mean",
    "rsn_std",
]

SELECTED_DEP = [
    "Aisne",
    "Alpes-Maritimes",
    "Ardèche",
    "Ariège",
    "Aude",
    "Aveyron",
    "Cantal",
    "Eure",
    "Eure-et-Loir",
    "Gironde",
    "Haute-Corse",
    "Hautes-Pyrénées",
    "Hérault",
    "Indre",
    "Landes",
    "Loiret",
    "Lozère",
    "Marne",
    "Oise",
    "Pyrénées-Atlantiques",
    "Pyrénées-Orientales",
    "Sarthe",
    "Somme",
    "Yonne",
]

LAG_ERA5T_VARS = [x for x in MODEL_ERA5T_VARS if "_lag" in x]

TEST_SIZE = 0.2

RANDOM_STATE = 42

RF_PARAMS = {
    "n_estimators": 500,
    "min_samples_leaf": 10,
    "max_features": "sqrt",
    "class_weight": "balanced",
    "criterion": "gini",
    "random_state": 10,
    "n_jobs": -1,
}

XGB_PARAMS = {
    "max_depth": 10,
    "min_child_weight": 10,
    "eta": 0.01,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "objective": "binary:logistic",
    "eval_metric": ["logloss", "aucpr"],
}
