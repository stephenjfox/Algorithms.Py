def k_folds(list_like, num_folds=10):
    """this expects a fixed-length list"""
    _len = len(list_like)
    step = _len // num_folds
    return [list_like[i:i+step] for i in range(0, _len, step)]


def _inner_fold_yield(folds_as_list, skip_index):
    for i, _list in enumerate(folds_as_list):
        if i is not skip_index:
            yield _list

def k_sample(folded_data, k_index=0):
    return list(_inner_fold_yield(folded_data, k_index)), folded_data[k_index]
