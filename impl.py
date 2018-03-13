def k_folds(list_like, num_folds=10):
    """this expects a fixed-length list"""
    _len = len(list_like)
    step = _len // num_folds
    return [list_like[i:i+step:step] for i in range(0, _len, step)]
