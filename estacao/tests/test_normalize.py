from estacao.normalize import Normalize


class TestNormalize:
    def test_has_ep_attribute(self):
        assert hasattr(Normalize(), 'ep')

    def test_ep(self):
        normalize = Normalize()
        ep = normalize.ep(18)
        expected = 20.681888606861104
        assert ep == expected
