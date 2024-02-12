<script lang="ts">
    import "../../styles/global.css";
    import "../../styles/offre.css";
  
    import Button from "../../Components/Inputs/Button.svelte";
    import Link from "../../Components/Inputs/Link.svelte";
    import type { Offre } from "../../Models/Offre";
  
    let offre: Offre = {
    titre: "",
    employeur: "",
    periodeJour: false,
    periodeSoir: false,
    periodeNuit: false,
    periodeFinDeSemaine: false,
    saisonHiver: false,
    saisonEte: false,
    saisonAutomne: false,
    saisonPrintemps: false,
    heure : "",
    salaire: "",
    stage: true,
    duree: "",
    programme: "",
    conciliation: "", 
    urgente: false,
    lien: "",
    description: "",
    dateAffichageDebut: "", 
    dateAffichageFin: "",
    personneContact: "",
    courrielContact: "",
    telephoneContact: "",
    };
  
    function handleSubmit() {
      // Here you can handle form submission, for now, just logging the values
      console.log(offre);
    }
  </script>
  
  <div class="container">
    <h1>Créer un offre d'emplois</h1>
  
    <form on:submit|preventDefault={handleSubmit} class="form-offre">
      <div class="form-group-horizontal">
        <label for="titre">Titre</label>
        <input type="text" bind:value={offre.titre} class="form-control" id="titre" />
      </div>
      <div class="form-group-horizontal">
        <label for="employeur">Employeur</label>
        <input type="text" bind:value={offre.employeur} class="form-control" id="employeur" />
      </div>
      <div class="form-group-horizontal">
        <label for="periode">Période</label>
        <div class="list-check">
          <label for="periode">Jour</label>
          <input type="checkbox" bind:checked={offre.periodeJour} class="form-control" id="periodeJour" />
        </div>
        <div class="list-check">
          <label for="periode">Soir</label>
          <input type="checkbox" bind:checked={offre.periodeSoir} class="form-control" id="periodeSoir" />
        </div>
        <div class="list-check">
          <label for="periode">Nuit</label>
          <input type="checkbox" bind:checked={offre.periodeNuit} class="form-control" id="periodeNuit" />
        </div>
        <div class="list-check">
          <label for="periode">Fin de Semaine</label>
          <input type="checkbox" bind:checked={offre.periodeFinDeSemaine} class="form-control" id="periodeFinDeSemaine" />
        </div>
      </div>
      <div class="form-group-horizontal">
        <label for="salaire">Salaire</label>
        <input type="text" bind:value={offre.salaire} class="form-control" id="salaire" />
      </div>
      <div class="form-group-horizontal">
        <label for="heure">Heure</label>
        <input type="text" bind:value={offre.heure} class="form-control" id="heure" />
      </div>
      <div class="form-group-horizontal">
        <label for="stage">Stage</label>
        <input type="checkbox" bind:checked={offre.stage} class="form-control" id="stage" />
      </div>
      <div class="form-group-horizontal">
        <label for="duree">Durée</label>
        <input type="text" bind:value={offre.duree} class="form-control" id="duree" />
      </div>
      <div class="form-group-horizontal">
        <label for="programme">Programme</label>
        <input type="text" bind:value={offre.programme} class="form-control" id="programme" />
      </div>
      <div class="form-group-horizontal">
        <label for="conciliation">Conciliation</label>
        <input type="text" bind:value={offre.conciliation} class="form-control" id="conciliation" />
      </div>
      <div class="form-group-horizontal">
        <label for="urgente">Urgente</label>
        <input type="checkbox" bind:checked={offre.urgente} class="form-control" id="urgente" />
      </div>
    </form>
    
  </div>
  