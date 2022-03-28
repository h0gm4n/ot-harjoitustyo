import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(10)

    def test_rahamaara_ja_myytyjen_maara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateisosto_toimii(self):
        #
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_kateisosto_palauttaa_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(260), 20)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_kateisosto_ei_onnistu_jos_saldo_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_kateisosto_toimii(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_kateisosto_palauttaa_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(420), 20)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_kateisosto_ei_onnistu_jos_saldo_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(380), 380)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_onnistuu_jos_saldo_riittaa_edullinen(self):
        #
        self.maksukortti.lataa_rahaa(240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_ei_onnistu_jos_saldo_ei_riita_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_onnistuu_jos_saldo_riittaa_maukas(self):
        self.maksukortti.lataa_rahaa(400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_ei_onnistu_jos_saldo_ei_riita_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_rahan_laataminen_toimii(self):
        #
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_rahan_negatiivinen_lataaminen_ei_toimi(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
