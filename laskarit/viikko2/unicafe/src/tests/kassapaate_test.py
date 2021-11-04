import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
        self.eurokortti = Maksukortti(100)

    #kassapääte yleiset

    def test_luodun_kassapaatteen_myydyt_lounaat_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat + self.kassapaate.edulliset, 0)

    def test_luodun_kassapaatteen_saldo_tuhat(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    #käteisostot maukas

    def test_kateisosto_lisää_kassaan_rahaa_maukkaalla_lounaalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_antaa_oikein_vaihtorahan_rahaa_maukkaalla_lounaalla(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)

    def test_kateisosto_lisaa_kassaan_lyodyn_lounaan_maukkaalla_lounaalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_palauttaa_liian_pienen_maksun_maukkaalla_lounaalla(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)

    def test_kateisosto_ei_lisaa_kassaan_lounasta_liian_pienella_maksulla_maukkaalla_lounaalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_ei_lisaa_kassaan_rahaa_liian_pienella_maksulla_maukkaalla_lounaalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    #käteisostot edullinen

    def test_kateisosto_lisää_kassaan_rahaa_edullisella_lounaalla(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_antaa_oikein_vaihtorahan_rahaa_edukkaalla_lounaalla(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, 260)

    def test_kateisosto_lisaa_kassaan_lyodyn_lounaan_edukkaalla_lounaalla(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_palauttaa_liian_pienen_maksun_edukkaalla_lounaalla(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)

    def test_kateisosto_ei_lisaa_kassaan_lounasta_liian_pienella_maksulla_edukkaalla_lounaalla(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_ei_lisaa_kassaan_rahaa_liian_pienella_maksulla_edukkaalla_lounaalla(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    #korttiostot maukas

    def test_korttiosto_onnistuu_maukkaalla_lounaalla(self):
        palautettava_boolean = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(palautettava_boolean, True)

    def test_korttiosto_veloitetaan_kortilta_maukkaalla_lounaalla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 600)

    def test_korttiosto_lyodaan_kassaan_maukkaalla_lounaalla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_ei_onnistu_maukkaalla_lounaalla_kun_kortin_saldo_ei_riita(self):
        palautettava_boolean = self.kassapaate.syo_maukkaasti_kortilla(self.eurokortti)
        self.assertEqual(palautettava_boolean, False)

    def test_korttiostoa_ei_veloiteta_kortilta_maukkaalla_lounaalla_kun_kortin_saldo_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.eurokortti)
        self.assertEqual(self.kortti.saldo, 1000)

    def test_korttiostoa_ei_lyoda_kassaan_maukkaalla_lounaalla_kun_kortin_saldo_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.eurokortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    #korttiostot edukas

    def test_korttiosto_onnistuu_edukkaalla_lounaalla(self):
        palautettava_boolean = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(palautettava_boolean, True)

    def test_korttiosto_veloitetaan_kortilta_edukkaalla_lounaalla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 760)

    def test_korttiosto_lyodaan_kassaan_edukkaalla_lounaalla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_ei_onnistu_edukkaalla_lounaalla_kun_kortin_saldo_ei_riita(self):
        palautettava_boolean = self.kassapaate.syo_edullisesti_kortilla(self.eurokortti)
        self.assertEqual(palautettava_boolean, False)

    def test_korttiostoa_ei_veloiteta_kortilta_edukkaalla_lounaalla_kun_kortin_saldo_ei_riita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.eurokortti)
        self.assertEqual(self.kortti.saldo, 1000)

    def test_korttiostoa_ei_lyoda_kassaan_edukkaalla_lounaalla_kun_kortin_saldo_ei_riita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.eurokortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    #kortin saldon lataus
    
    def test_kortille_rahaa_ladatessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kortti.saldo, 1100)

    def test_kortille_rahaa_ladatessa_kassan_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kortti.saldo, 1000)

    def test_kortille_negatiivista_summaa_yrittaessa_kassan_rahasumma_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
