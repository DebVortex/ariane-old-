from ariane.apps.core import register, register_js


class TestArianeAppRegistration:
    """Test the module registration process."""

    def test_register(self, clean_ariane, languages):
        """Test the register function."""

        def example_func():
            pass

        register(languages, example_func)
        for language in languages:
            for keyword in clean_ariane._brain[language]:
                assert clean_ariane._brain[language][keyword] == example_func

    def test_register_js(self, clean_ariane, jsfile_path):
        """Test the register_js function."""
        register_js(jsfile_path)
        assert jsfile_path in clean_ariane.js_files
