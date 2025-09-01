
let a = await fetch("https://lemida.biu.ac.il/", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "block-fcl_d23f31569bc38088af5e2b219267ad5d=collapsed; block-fcl_cfa41beeb55b62d668ccc14c4e2da36a=collapsed; block-fcl_d53488db418342d3df30b1e19a8d97f5=collapsed; block-fcl_58d06c0953abecce5a385e8eaee547fa=collapsed; block-fcl_93690d25f45d380973729de31b01cfd8=collapsed; block-fcl_01bc73db55e9ae01e71f8a079400374d=collapsed; block-fcl_c0c8b7daafe6530bbd6f9dfd92cabfb2=collapsed; block-fcl_3dfcf5b8d063a3b3270d9edcac58a4ed=collapsed; block-fcl_e21962ca69de8b6e0bb6daa3bfd04277=collapsed; block-fcl_a9b3e828bdb9e6e3393387edde482b6b=collapsed; _ga_7GX8H63VHT=GS1.1.1742396531.1.1.1742397513.0.0.0; _vwo_uuid_v2=D5C1D9C3280D67F07DA9465594CAE0DFA|7eed07a374da2d1780b3a31befd8f903; _fbp=fb.2.1742397519531.663761372931520106; _vwo_uuid=D5C1D9C3280D67F07DA9465594CAE0DFA; _vis_opt_test_cookie=1; icVrId=2c1c5ee1-be5c-6869-0826-cfa607ad0cc8; glassix-visitor-id-v2-a274588e-2e78-4195-bc11-5b9abfecff68=d30d11d5-df67-4a94-ba0c-06344d0a9c9c; _tt_enable_cookie=1; _ttp=01JPQMY4RKZTY7CMNY8W0437DC_.tt.2; block-fcl_939c134b8c5e98d785934aabe5f579f9=expanded; _ga_0R9T78TGGK=GS1.1.1742402948.1.0.1742404369.0.0.0; __ssds=3; __ssuzjsr3=a9be0cd8e; __uzmbj3=1742929969; block-fcl_1245de9de4ee9180b7b6171b116b3ea6=expanded; block-fcl_5145b449e0d22fa8bc5dd84bdbe324fd=expanded; __uzmaj3=cfaf956e-b37b-422e-814a-3dd322bdb23f; __uzmlj3=mzP0c75AxVrTIkFA2PrkgQSj+gZ4vmJKUSnyCuTrHf4=; uzmx=7f900067a868b3-7430-4deb-acd5-41dc26b9a5305-17429299689484069534823-795121ee28cca8da187; __uzmcj3=460446768779; __uzmdj3=1746999504; __uzmfj3=7f6000042e0bbc-91f2-48a6-83c5-e7d6d7524df417429299694574069534643-cded2f07c6a7160367; uzmxj=7f900067a868b3-7430-4deb-acd5-41dc26b9a5305-17429299694574069534643-a0933df00374bd6267; _ga_S8SZC9BRW6=GS2.1.s1748460974$o1$g0$t1748460974$j60$l0$h0; _gcl_au=1.1.870292433.1752472885; icreate_visitor_guid=2c1c5ee1-be5c-6869-0826-cfa607ad0cc8; _hjSessionUser_2646769=eyJpZCI6ImM4N2U4ZTYyLTE5OWMtNTcwZS05MWFhLTZiODk0MWNkNjljNCIsImNyZWF0ZWQiOjE3NDIzOTc1MTg5NTksImV4aXN0aW5nIjp0cnVlfQ==; block-fcl_9873bc3f7374fae127c196a87cb3d350=collapsed; block-fcl_b91fd6c119a4e54d35b4fdf094109dd9=collapsed; _ga_TC78MYLYGV=GS2.1.s1755201781$o3$g1$t1755201795$j46$l0$h0; _ga=GA1.1.1858160117.1742396531; _ga_2Y2ZKLWX5C=GS2.1.s1755680595$o4$g0$t1755680595$j60$l0$h0; ph_phc_szLwxKe8adfTV0DGCaojRxPhXTKemUDztgsJffjMOah_posthog=%7B%22distinct_id%22%3A%2201980786-1854-7dad-9da6-e2243bc88a56%22%2C%22%24sesid%22%3A%5B1755680595417%2C%220198c6b7-dddb-71a8-bf07-efd3da4a3b17%22%2C1755680595417%5D%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fyesod.biu.ac.il%2Fnode%2F1375%22%7D%7D; _ga_KFGJ7S0N40=GS2.1.s1755680595$o14$g0$t1755680595$j60$l0$h0; block-fcl_1845493dc07e3017941a5d7cb0048498=expanded; MoodleSessionprod=1ll0muo9s2uube76hkkensnvop"
    ,"Referer": "a"
  },
  "body": null,
  "method": "GET"
});

console.log(await a.text())