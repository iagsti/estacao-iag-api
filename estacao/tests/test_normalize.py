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

    def test_has_rh_tw_attribute(self):
        assert hasattr(Normalize(), 'rh_tw')

    def test_rh_tw(self):
        expected = 62.96058499472006
        normalize = Normalize()
        p = normalize.trans_p(698.9, 25.0)
        rh = normalize.rh_tw(26.9, 21.5, p)
        assert rh == expected
