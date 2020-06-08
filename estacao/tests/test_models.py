class TestConsolidado:
    def test_consolidado_length(self, consolidado):
        assert len(consolidado) == 1

    def test_has_save_attribute(self, consolidado):
        assert hasattr(consolidado[0], 'save')
