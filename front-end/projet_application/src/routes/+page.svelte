<script lang="ts">
  import "../styles/global.css";
  import Header from "../Components/Common/Header.svelte";
  import Footer from "../Components/Common/Footer.svelte";
  import Button from "../Components/Inputs/Button.svelte";
</script>

<Header />
<main>
  <section class="haut">
    <div class="haut-gauche">
      <h1 class="title">
        <span>PORTAIL D'</span><span>OFFRES D'EMPLOI</span>
      </h1>
      <h2>DU CÉGEP DE RIVIÈRE-DU-LOUP</h2>
    </div>
    <div class="haut-droite">
      <Button text="Consulter toutes les offres" />
    </div>
  </section>
</main>
<Footer />

<style scoped>
  h2 {
    color: white;
  }
  .title {
    left: 7.2%;
  }
  .title span:first-child {
    color: white;
    margin: 0;
  }
  .title span:last-child {
    color: #00ad9a;
    margin: 0;
  }

  main {
    display: flex;
    flex-direction: column;
    width: 100%;
  }
  .haut {
    display: flex;
    widows: 85%;
  }
  .haut-gauche {
    display: flex;
    flex-direction: column;
    width: 50%;
    left: 7.2%;
  }
  .haut-droite {
    width: 50%;
  }
</style>
