def k_folds(data_to_fold: list, num_folds: int=10):
    """this expects a fixed-length list

    Keyword arguments:
    num_folds -- the num of desired folds to data to produce
    """
    _len = len(data_to_fold)
    step = _len // num_folds
    return [data_to_fold[i:i+step] for i in range(0, _len, step)]


# TODO: Write a function that randomly shuffles the folded data.

def _inner_fold_yield(folds_as_list: list, skip):
    test = lambda elem: elem not in skip if skip is list else elem is not skip
    for i, _list in enumerate(folds_as_list):
        if test(i):
            yield _list

def k_sample(folded_data, index=0):
    """Splits the folded data into training and validation sets.
    Arguments:
    folded_data -- a list of list, preferably output by k_folds

    Keyword arguments:
    index -- either an integer or list of integers. As a result, the validation
             set will be a single list or a list of lists, respectively
    """
    training_set = list(_inner_fold_yield(folded_data, index))
    if type(index) is list:
        return training_set, [folded_data[v] for v in index]
    else:
        return training_set, folded_data[index]
