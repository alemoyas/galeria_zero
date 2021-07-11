//nadbar para la sesion iniciada
$(document).ready(function() {
    $("#nadvar_si").html(`<div class="container-fluid">
  <img src="../Imagenes/recursos/logo.jpg" alt="imagen" height="60px" width="60px">
  &nbsp&nbsp
  <a class="navbar-brand" href="../Index_sesion_iniciada.html">Grupo Cero</a>
  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
  <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
  <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link" href="../vistas/subir.html">Subir Obra</a>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="../vistas/Evaluar.html">Evaluar Obras</a>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="../index.html">Salir</a>
        </li>
  </ul>
  <form class="d-flex">
    <input class="form-control me-2" type="search" placeholder="Buscar" aria-label="Search">
    <button class="btn btn-outline-success" type="submit">Buscar</button>
  </form>
  </div>
  </div>`);
  
  })
