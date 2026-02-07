def calculate_confidence(ocr_conf, cv_conf, agreement):
    return round(
        0.4 * ocr_conf +
        0.3 * cv_conf +
        0.3 * agreement,
        2
    )
