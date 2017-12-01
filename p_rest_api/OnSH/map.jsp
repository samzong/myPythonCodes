<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
<style type="text/css">
body, html,#allmap {width: 100%;height: 100%;overflow: hidden;margin:0;}
#l-map{height:100%;width:78%;float:left;border-right:2px solid #bcbcbc;}
#r-result{height:100%;width:20%;float:left;}
</style>
<script type="text/javascript" src="http://api.map.baidu.com/api?v=2.0&ak=AsnQt6acECu8FGhmXbm2aTEG"></script>
<title>添加多个标注点</title>
</head>
<body>
<div id="allmap"></div>
</body>
</html>
<script type="text/javascript">


// 百度地图API功能
/* var sContent =
"<h4 style='margin:0 0 5px 0;padding:0.2em 0'>大观楼</h4>" + 
"<img style='float:right;margin:4px' id='imgDemo' src='https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSdw1MsiOkIAsEjSrYiwUPiURRpWO2rJGx899zNVcqBN19OwHvjmg' width='139' height='104' title='大观楼'/>" + 
"<p style='margin:0;line-height:1.5;font-size:13px;text-indent:2em'>昆明大观楼，在大观公园，位于滇池北滨，距市中心约6千米...</p>" + 
"</div>"; */

// 百度地图API功能
var map = new BMap.Map("allmap");
	
var objs = [{ longitude: 102.680412, latitude: 25.030081,title:"大观楼",imgUrl:"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSdw1MsiOkIAsEjSrYiwUPiURRpWO2rJGx899zNVcqBN19OwHvjmg",description:"昆明大观楼，在大观公园，位于滇池北滨，距市中心约6千米." }, { longitude: 102.677582, latitude: 25.028845,title:"大观楼停车场",imgUrl:"http://imgt0.bdstatic.com/it/u=3535641568,2312771970&fm=21&gp=0.jpg",description:"大观楼的停车场,停车方便,交通便捷..."}];
start(objs);
function start(objs){
	for(var i=0;i<objs.length;i++) {
		point = new BMap.Point(objs[i].longitude,objs[i].latitude);
		content = doContent(objs[i].title,objs[i].imgUrl,objs[i].description);
		addMarker(point,content);
	};
}	

//自定义一个函数用于拼接显示内容
function doContent(title,imgUrl,description) {
	return "<h4 style='margin:0 0 5px 0;padding:0.2em 0'>"+title+"</h4>" + 
			"<img style='float:right;margin:4px' id='img' src='"+imgUrl+"' width='139' height='104' title='"+title+"'/>" + 
			"<p style='margin:0;line-height:1.5;font-size:13px;text-indent:2em'>"+description+"</p>" + 
			"</div>";
}

// 编写自定义函数,创建标注
function addMarker(point,content){
	var marker = new BMap.Marker(point);
	//var infoWindow = new BMap.InfoWindow(sContent); 
	var infoWindow = new BMap.InfoWindow(content); 
	map.addOverlay(marker);
	marker.addEventListener("click", function(){          
		this.openInfoWindow(infoWindow);
		//图片加载完毕重绘infowindow
		document.getElementById('imgDemo').onload = function (){
		    infoWindow.redraw();   //防止在网速较慢，图片未加载时，生成的信息框高度比图片的总高度小，导致图片部分被隐藏
		};
	});
}
map.centerAndZoom(point, 15);
map.enableScrollWheelZoom(); //启用滚轮放大缩小
</script>
