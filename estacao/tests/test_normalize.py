from estacao.normalize import Normalize


class TestNormalize:
    def test_has_ep_attribute(self):
        assert hasattr(Normalize(), 'ep')

    def test_ep(self):
        normalize = Normalize()
        ep = normalize.ep(18)
        expected = 20.681888606861104
        assert ep == expected

    def test_has_trans_p(self):
        assert hasattr(Normalize(), 'trans_p')

    def test_trans_p(self):
        expected = 926.2597977212171
        normalize = Normalize()
        trans_p = normalize.trans_p(698.9, 25.0)
        assert trans_p == expected
