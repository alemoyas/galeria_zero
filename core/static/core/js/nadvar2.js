//nadbar
$(document).ready(function() {
    $("#nadvar").html(`<div class="container-fluid">
  <img src="../Imagenes/recursos/logo.jpg" alt="imagen" height="60px" width="60px">
  &nbsp&nbsp
  <a class="navbar-brand" href="../index.html">Grupo Cero</a>
  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
  <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
  <ul class="navbar-nav me-auto mb-2 mb-lg-0">
    <li class="nav-item dropdown">
      <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
        Categorias
      </a>
      <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
        <li><a class="dropdown-item" href="../categorias/categoria_escultores.html">Categoria Escultores</a></li>
        <li><a class="dropdown-item" href="../categorias/categoria_orfebres.html">Categoria Orfebres</a></li>
        <li><a class="dropdown-item" href="../categorias/categoria_pintores.html">Categoria Pintores</a></li>
        <li><a class="dropdown-item" href="../categorias/categoria_tejedor.html">Categoria Tejedores</a></li>
      </ul>
    <li class="nav-item dropdown">
      <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
        Galerias
      </a>
      <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
        <li><a class="dropdown-item" href="../galerias/galeria_generica_Van_Gogh.html">Galeria de Vincent van Gogh</a></li>
        <li><a class="dropdown-item" href="../galerias/galeria_generica_Picasso.html">Galeria de Picasso</a></li>
        <li><a class="dropdown-item" href="../galerias/galeria_generica_Andres_Lupin.html">Galeria de Andres</a></li>
        <li><a class="dropdown-item" href="../galerias/galeria_generica_Donatello.html">Galeria de Donatello</a></li>
        <li><a class="dropdown-item" href="../galerias/galeria_generica_Leandro.html">Galeria de Leandro</a></li>
        <li><a class="dropdown-item" href="../galerias/galeria_generica_Marcelo.html">Galeria de Marcelo</a></li>
        <li><a class="dropdown-item" href="../galerias/galeria_generica_Miguel_angel.html">Galeria de Miguel Angel</a></li>
        <li><a class="dropdown-item" href="../galerias/galeria_generica_Pablo.html">Galeria de Pablo</a></li>
      </ul>
    <li class="nav-item dropdown">
      <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
        Artistas
      </a>
      <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
        <li><a class="dropdown-item" href="../Pintores/ficha_autor_Van_Gogh.html">Vincent van Gogh</a></li>
        <li><a class="dropdown-item" href="../Pintores/ficha_autor_Picasso.html">Picasso</a></li>
        <li><a class="dropdown-item" href="../escultores/donatello.html">Donatello</a></li>
        <li><a class="dropdown-item" href="../escultores/miguel_angel.html">Miguel Angel</a></li>
        <li><a class="dropdown-item" href="../orfebres/marcelo_cumplido.html">Marcelo</a></li>
        <li><a class="dropdown-item" href="../orfebres/pablo_rodriguez.html">Pablo</a></li>
        <li><a class="dropdown-item" href="../tejedores/leandro_bonatelli.html">Leandro</a></li>
        <li><a class="dropdown-item" href="../tejedores/andres_lupin.html">Andres Lupin</a></li>
      </ul>
      <li class="nav-item">
          <a class="nav-link" href="../vistas/Iniciar_sesion.html">Iniciar sesion</a>
        </li>
        
       <li class="nav-item">
          <a class="nav-link" href="../vistas/Registrarse.html">Resgistrarse</a>
        </li>
        
        <li class="nav-item">
          <a class="nav-link" href="../vistas/Formulario.html">Contacto</a>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="../Galeria_chicago/chicagoGaleria.html">Galeria Chicago</a>
        </li>
  </ul>
  <form class="d-flex">
    <input class="form-control me-2" type="search" placeholder="Buscar" aria-label="Search">
    <button class="btn btn-outline-success" type="submit">Buscar</button>
  </form>
  </div>
  </div>`);
  
  })