
<template>

    <div class="carrousel">
        <div class="tapa" id="move">
          <div class="item"><img src="https://phonoteka.org/uploads/posts/2021-05/1621961575_39-phonoteka_org-p-pikselnie-arti-krasivo-40.jpg"></div>
          <div class="item"><img src="https://phonoteka.org/uploads/posts/2021-05/1621961575_39-phonoteka_org-p-pikselnie-arti-krasivo-40.jpg"></div>
          <div class="item"><img src="https://phonoteka.org/uploads/posts/2021-05/1621961575_39-phonoteka_org-p-pikselnie-arti-krasivo-40.jpg"></div>
          <div class="item"><img src="https://phonoteka.org/uploads/posts/2021-05/1621961575_39-phonoteka_org-p-pikselnie-arti-krasivo-40.jpg"></div>
          <div class="item"><img src="https://phonoteka.org/uploads/posts/2021-05/1621961575_39-phonoteka_org-p-pikselnie-arti-krasivo-40.jpg"></div>
          <div class="item"><img src="https://phonoteka.org/uploads/posts/2021-05/1621961575_39-phonoteka_org-p-pikselnie-arti-krasivo-40.jpg"></div>
          <div class="item"><img src="https://phonoteka.org/uploads/posts/2021-05/1621961575_39-phonoteka_org-p-pikselnie-arti-krasivo-40.jpg"></div>
          <div class="item"><img src="https://phonoteka.org/uploads/posts/2021-05/1621961575_39-phonoteka_org-p-pikselnie-arti-krasivo-40.jpg"></div>
          <div class="item"><img src="https://phonoteka.org/uploads/posts/2021-05/1621961575_39-phonoteka_org-p-pikselnie-arti-krasivo-40.jpg"></div>
          <div class="item"><img src="https://phonoteka.org/uploads/posts/2021-05/1621961575_39-phonoteka_org-p-pikselnie-arti-krasivo-40.jpg"></div>
            <!-- Otras imágenes aquí -->
        </div>
        <!-- Controles -->
        <div class="cont">
            <div class="left controls" id="l"><img src="https://cdn2.iconfinder.com/data/icons/electronic-line-3/64/back_Arrow_chevron_left_ui_interface_icon-512.png"></div>
            <div class="right controls" id="r"><img src="https://cdn1.iconfinder.com/data/icons/mixed-17/16/icon_right_rounded-512.png"></div>
        </div>
    </div>
</template>


<script>


        let x = 0;
        let p = -10;
        let i = 1;
        
        let doom = document.getElementsByClassName('item');
        let confr = (doom.length - 3) * (-350);
        let confl = 0;

// Botón izquierdo
document.getElementById("l").addEventListener("click", function () {
    x += 350;
    if (x > confl) {
        x = confr - 350;
    } else {
        document.getElementById("move").style.marginLeft = x + "px";
    }
});

// Botón derecho
document.getElementById("r").addEventListener("click", function () {
    x += -350;
    p += -10;
    if (x < confr) {
        x = 350;
    } else {
        document.getElementById("move").style.marginLeft = x + "px";
    }
});

</script>


<style>
        body {
		background-color: #444;
	}
	.controls {
		width: 42px;
		height: 42px;
		padding: 10px;
		border-radius: 0;
		cursor: pointer;
		background-color: rgba(0,0,0,0);
	}
.controls img {
    width: 100%; /* Ajustar el ancho de las imágenes al 100% del contenedor */
  height: auto; /* Ajustar la altura automáticamente */
}
	.left {
		position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    margin-left: -50px;
	}
	.right {
		position: absolute;
    top: 50%;
    right: 0;
    transform: translateY(-50%);
    margin-right: -70px;
	}
	.carrousel {
		width: 1100px;
		margin: auto;
		height: 450px;
		margin-top: 120px;
		overflow:hidden;
	}
	.controls:hover {
		background-color: rgba(0,0,0,.5);
	}
	.item {
		width: 335px;
		height: 400px;
		float: left;
		margin-left: 15px;
		margin-top: 20px;
		background-color: #202225;
		color: #fff;
		font-size: 40px;
		text-align: center;
		padding-top: 30px;
		border-radius: 5px;
		cursor: pointer;
	  transition: 1s all;
		/*box-shadow: 0 9px 10px rgba(6,6,7,.3);*/
	}
	.cont {
		position: absolute;
		width: 1100px;
		margin-top: 190px;
	}
	.tapa {
	  width: 12000px;/* 	change if the size is >     12000  :) */
		transition: .9s all;
	}
	.item img {
    width: 100%; /* Ajustar el ancho de las imágenes al 100% del contenedor */
    height: 100%; /* Ajustar la altura automáticamente para mantener la proporción */
    margin: 0; /* Eliminar cualquier margen por defecto */
    display: block; /* Cambiar a "block" para ajustar el ancho y el margen automáticamente */
    position: auto;
    top: 50%;
    left: 0;
}
	.item:hover {
		margin-top: -6px;
	}
</style>

