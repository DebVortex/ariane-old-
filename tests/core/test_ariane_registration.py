from ariane.apps.core import Ariane, register, register_js


class TestArianeAppRegistration:
    """Test the module registration process."""

    def test_register(self, clean_ariane, wit_access_token, language_code):
        """Test the register function."""
        @register('intent')
        def example_func():
            """Function to use in tests for ariane."""
            pass

        assert Ariane(language_code).actions['intent'] == example_func

    def test_register_js(self, clean_ariane, wit_access_token, language_code, jsfile_path):
        """Test the register_js function."""
        register_js(jsfile_path)
        assert any([jsfile_path in js_file[0] for js_file in Ariane(language_code).js_files])
