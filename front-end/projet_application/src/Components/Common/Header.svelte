<script lang="ts">
  import "../../styles/header.css";
  import Link from "../Inputs/Link.svelte";
</script>

<header class="">
  <div class="logo-img">
    <img src="./src/images/logo.png" class="image" alt="Logo" />
  </div>
  <div class="ul-group">
    <ul class="ul-menu">
      <li class="li-items"><Link href={"/"} text="Accueil" /></li>
      <li class="li-items"><Link href={"/login"} text="Se connecter" /></li>
    </ul>
  </div>
</header>
