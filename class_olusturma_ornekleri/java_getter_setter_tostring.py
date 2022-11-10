# package YeniProjeCalismalari.DepoYonetimi_v1;
#
# import java.util.HashMap;
#
# public class UrunTanimlama extends VeriDeposu{
#
#     private int id;
#     private String urunIsmi;
#     private String ureticiFirma;
#     private int miktar;
#     private String birim;
#     private String raf;
#     private int birimFiyat;
#     private int toplamFiyat;
#
#     public UrunTanimlama() {
#     }
#
#     public UrunTanimlama(int id, String urunIsmi, String ureticiFirma, String birim) {
#         this.id = id;
#         this.urunIsmi = urunIsmi;
#         this.ureticiFirma = ureticiFirma;
#         this.birim = birim;
#
#     }
#     public int getToplamFiyat() {
#         return toplamFiyat;
#     }
#
#     public void setToplamFiyat(int toplamFiyat) {
#         this.toplamFiyat = toplamFiyat;
#     }
#
#     public int getBirimFiyat() {
#         return birimFiyat;
#     }
#
#     public void setBirimFiyat(int birimFiyat) {
#         this.birimFiyat = birimFiyat;
#     }
#
#     public int getId() {
#         return id;
#     }
#
#     public void setId(int id) {
#         this.id = id;
#     }
#
#     public String getUrunIsmi() {
#         return urunIsmi;
#     }
#
#     public void setUrunIsmi(String urunIsmi) {
#         this.urunIsmi = urunIsmi;
#     }
#
#     public String getUreticiFirma() {
#         return ureticiFirma;
#     }
#
#     public void setUreticiFirma(String ureticiFirma) {
#         this.ureticiFirma = ureticiFirma;
#     }
#
#     public int getMiktar() {
#         return miktar;
#     }
#
#     public void setMiktar(int miktar) {
#         if (miktar<0){
#             this.miktar = 0;
#         }else{
#             this.miktar = miktar;
#         }
#
#     }
#
#     public String getBirim() {
#         return birim;
#     }
#
#     public void setBirim(String birim) {
#         this.birim = birim;
#     }
#
#     public String getRaf() {
#         return raf;
#     }
#
#     public void setRaf(String raf) {
#         this.raf = raf;
#     }
#
#     @Override
#     public String toString() {
#         return "UrunTanimlama{" +
#                 "id=" + id +
#                 ", urunIsmi='" + urunIsmi + '\'' +
#                 ", ureticiFirma='" + ureticiFirma + '\'' +
#                 ", miktar=" + miktar +
#                 ", birim='" + birim + '\'' +
#                 ", birim fiyatı='" + birimFiyat + '\'' +
#                 ", toplam fiyatı ='" + toplamFiyat + '\'' +
#                 ", raf='" + raf + '\'' +
#                 '}';
#     }
#
#
# }

input_x = "Clarusway"
for i in input_x:
    print(i, end="-")
