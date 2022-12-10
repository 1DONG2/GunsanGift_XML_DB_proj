<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="utf-8">
        <link  rel="stylesheet" href="../finalresult.css" type="text/css">
    </head>
    <body>
		<h1>군산의 모범식당 현황</h1>
		
		<form action="action.jsp">
			<div><input type="radio" name="special" value="ChackanStore"  onClick="location.href='http://localhost/splited/ChackanStore.php'">착한가격업소 보기</div>
			<div><input type="radio" name="special" value="GoodRestaurant"  onClick="location.href='http://localhost/splited/GoodRestaurant.php'">모범식당 보기</div>
			<div><input type="radio" name="special" value="GunsanGift"  onClick="location.href='http://localhost/splited/GunsanGift.php'">군산사랑상품권 가맹점 보기</div>
			<div><input type="radio" name="special" value="HoleIntheWall"  onClick="location.href='http://localhost/splited/HoleIntheWall.php'">맛집 보기</div>
			<div><input type="radio" name="special" value="MillenniumStore"  onClick="location.href='http://localhost/splited/MillenniumStore.php'">백년가게 보기</div>
			<div><input type="radio" name="special" value="MillenniumStore"  onClick="location.href='http://localhost/finalresult.php'">전체 보기</div>
		</form>

		<a href="http://localhost/Graphs.php">통계</a>
        <div id="map"></div>

        <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=b6a6fd01fad5e91b53d6ff10e0a8e509&libraries=services"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
        <script>
            var mapContainer = document.getElementById('map'),
            mapOption = { 
            center: new kakao.maps.LatLng(33.450701, 126.570667),
            level: 3
        };
		</script>
</br></br></br>
<script>

	var geocoder = new kakao.maps.services.Geocoder();
 
	var map = new kakao.maps.Map(mapContainer, mapOption); 

<?php
ini_set("memory_limit","2345M");

    			$xml = simplexml_load_file('../realfinalresult.xml');
    			$arr = $xml -> store;
    			foreach($arr as $row){
					$address = $row->RoadNameAddress;
					$legalName= $row->legalName;
					if($row->IsThisSpecial->IsThisGoodRestaurant=="O"){ //이쪽을 바꿔야함
						
					echo "geocoder.addressSearch('$address', function(result, status) {
							
						if (status === kakao.maps.services.Status.OK) {
						
							var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
						
							var marker = new kakao.maps.Marker({
								map: map,
								position: coords
							});
						
							var infowindow = new kakao.maps.InfoWindow({
								content: '<div style=\"width:150px;text-align:center;padding:6px 0;\">$legalName</div>'
							});
							infowindow.open(map, marker);
						
							map.setCenter(coords);
						} 
					});";
					 
    			    }
                }

				
			?>
		</script>
	
    <?php
    $data = "";
    $data .= "<table>";
    $data .= "<th>순번</th><th>업소명</th><th>업종</th><th>도로명주소</th><th>행정동</th><th>전화번호</th><th>군산사랑상품권</th>";
    if (file_exists('../realfinalresult.xml')) {
        $xml = simplexml_load_file('../realfinalresult.xml');
        $arr = $xml -> store;
       
        foreach($arr as $row){
            if($row->IsThisSpecial->IsThisGoodRestaurant=="O"){ //이쪽을 바꿔야함
                $data .= "<tr>";
                $data .= "<td id=". $row['id'] ." IsThisGunsanGift=". $row->IsThisSpecial->IsThisGunsanGift .">" . $row['id'] . "</td>";
                $data .= "<td>" . $row->legalName . "</td>";
                $data .= "<td>" . $row->category . "</td>";
                $data .= "<td>" . $row->RoadNameAddress . "</td>";
                $data .= "<td>" . $row->AdministrativeNeighborhood . "</td>";
                $data .= "<td>" . $row->telephone . "</td>";
                $data .= "<td>" . $row->IsThisSpecial->IsThisGunsanGift . "</td>";
                $data .= "</tr>";
            }
            
        }
        $data .= "</table>";
    } else {
        exit('망함');
    }
    ?>
    <?php echo $data; 
	?>

    </body>
</html>

