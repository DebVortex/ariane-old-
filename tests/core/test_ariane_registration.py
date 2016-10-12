from ariane.apps.core import Ariane, register, register_js


class TestArianeAppRegistration:
    """Test the module registration process."""

    def test_register(self, clean_ariane):
        """Test the register function."""
        def example_func():
            pass

        register('intent', example_func)
        assert Ariane()._brain['intent'] == example_func

    def test_register_js(self, clean_ariane, jsfile_path):
        """Test the register_js function."""
        register_js(jsfile_path)
        assert any([jsfile_path in js_file[0] for js_file in Ariane().js_files])
