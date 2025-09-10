import pytest
import estadistica

# MEDIA
def test_media_happy_path():
    assert estadistica.media([1, 2, 3, 4]) == 2.5
    assert estadistica.media([10, 20, 30]) == 20

def test_media_error():
    with pytest.raises(ValueError):
        estadistica.media([])

# MEDIANA
def test_mediana_happy_path():
    assert estadistica.mediana([1, 3, 2]) == 2
    assert estadistica.mediana([1, 2, 3, 4]) == 2.5

def test_mediana_error():
    with pytest.raises(ValueError):
        estadistica.mediana([])

# MODA
def test_moda_happy_path():
    assert estadistica.moda([1, 1, 2, 3]) == 5
    assert set(estadistica.moda([1, 2, 2, 3, 3])) == {2, 3}

def test_moda_error():
    with pytest.raises(ValueError):
        estadistica.moda([1, 2, 3])  # sin moda

# VARIANZA
def test_variance_happy_path():
    assert round(estadistica.variance([1, 2, 3, 4]), 2) == 1.25
    assert estadistica.variance([5, 5, 5]) == 0

def test_variance_error():
    with pytest.raises(ValueError):
        estadistica.variance([])

# DESVIACIÓN ESTÁNDAR
def test_ds_happy_path():
    assert round(estadistica.ds([1, 2, 3, 4]), 2) == 1.12
    assert estadistica.ds([5, 5, 5]) == 0

def test_ds_error():
    with pytest.raises(ValueError):
        estadistica.ds([])
