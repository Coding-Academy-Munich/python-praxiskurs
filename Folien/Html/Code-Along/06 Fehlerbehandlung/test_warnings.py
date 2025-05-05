# %% tags=["keep"]
import pytest
import warnings

# %% tags=["keep"]
# Assume calculate_old and check_value functions exist from previous example
def calculate_old(x):
    warnings.warn("Use calculate_new", DeprecationWarning, stacklevel=2)
    return x * 0.9

def check_value(v):
    if v > 100:
        warnings.warn("Value might be unstable", RuntimeWarning, stacklevel=2)
    return True

# %%
def test_calculate_old_warns():
    """Verify calculate_old issues the correct DeprecationWarning."""
    with pytest.warns(DeprecationWarning, match="Use calculate_new"):
        calculate_old(50)

# %%
def test_check_value_warns_if_high():
    """Verify check_value issues RuntimeWarning for high values."""
    with pytest.warns(RuntimeWarning, match="unstable"):
        check_value(200)

# %%
def test_check_value_does_not_warn_if_low():
    """Verify check_value issues NO warning for low values."""
    with warnings.catch_warnings(record=True) as captured:
        # Ensure warnings aren't filtered out by other settings during test
        warnings.simplefilter("always")
        check_value(50)
        # Assert no warnings were captured
        assert len(captured) == 0, f"Expected no warnings, got {len(captured)}"

# To run: pytest test_warnings.py
