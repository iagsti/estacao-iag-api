class TestConsolidado:
    def test_consolidado_length(self, consolidado):
        assert len(consolidado) == 1

    def test_has_save_attribute(self, consolidado):
        assert hasattr(consolidado[0], 'save')


class TestPressao:
    def test_pressao_length(self, pressao):
        assert len(pressao) == 1

    def test_has_save_attribute(self, pressao):
        assert hasattr(pressao[0], 'save')
