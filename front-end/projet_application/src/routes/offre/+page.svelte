<script lang="ts">
    import "../../styles/global.css";
    import "../../styles/offre.css";
  
    import Button from "../../Components/Inputs/Button.svelte";
    // import { MultiSelect } from "carbon-components-svelte"; -----------------
    import MultiSelect from 'svelte-multiselect';
    import type { Offre } from "../../Models/Offre";
  
    let offre: Offre = {
    titre: "",
    lieu: "",
    dateEntreeFontion: new Date(),
    heure : "",
    salaire: "",
    stage: true,
    duree: "",
    programme: "",
    conciliation: false, 
    urgente: false,
    lien: "",
    description: "",
    dateAffichageDebut: "", 
    dateAffichageFin: "",
    personneContact: "",
    courrielContact: "",
    telephoneContact: "",
    active: true,
    };

    let programmeSelected: { label: string; value: number }[] = [];
    let programmes = [
    { label: "Design d'intérieur", value: 1 },
    { label: "Éducation à l'enfance", value: 2 },
    { label: "Gestion et intervention en loisir", value: 3 },
    { label: "Graphisme", value: 4 },
    { label: "Informatique", value: 5 },
    { label: "Inhalothérapie", value: 6 },
    { label: "Pharmacie", value: 7 }
];
  let typeEmploisSelected: { label: string; value: number }[] = [];
      let typeEmplois = [
      { label: "Temps plein", value: 1 },
      { label: "Emploi d'été", value: 2 },
      { label: "Temps partiel", value: 3 },
      { label: "Stage", value: 4 },
  ];


    function handleSubmit() {
      // Here you can handle form submission, for now, just logging the values
      console.log(programmeSelected);
      console.log(offre);
    }
  </script>
  
  <div class="container">
    <form on:submit|preventDefault={handleSubmit} class="form-offre">
      <h1>Créer une nouvelle offre d'emploi</h1>
      <div class="form-group-horizontal">
        <label for="titre">Titre du poste*</label>
        <input type="text" bind:value={offre.titre} class="form-control" id="titre" />
      </div>
      <div class="form-group-horizontal">
        <label for="typeEmplois">Type d'emplois*</label>
        <MultiSelect
          id="periode"
          options={typeEmplois}
          placeholder="Choisir période(s)..."
          bind:value={typeEmploisSelected}
        />
      </div>
      <div class="form-group-horizontal">
        <label for="lieu">Lieu de travail*</label>
        <input type="text" bind:value={offre.lieu} class="form-control" id="salaire" />
      </div>
      <div class="form-group-horizontal">
        <label for="description">Description du poste*</label>
        <input type="text" bind:value={offre.description} class="form-control" id="salaire" />
      </div>
      <div class="form-group-horizontal">
        <label for="dateEntree">Date d'entrée en fonction</label>
        <input type="date" bind:value={offre.dateEntreeFontion} class="form-control" id="dateEntree" />
      </div>
      <div class="form-group-horizontal">
        <label for="dateLimite">Date limite pour postuler</label>
        <input type="date" bind:value={offre.dateLimitePostuler} class="form-control" id="dateLimite" />
      </div>
      <div class="form-group-horizontal">
        <label for="duree">Durée</label>
        <input type="text" bind:value={offre.duree} class="form-control" id="duree" />
      </div>
      <div class="form-group-horizontal">
        <label for="duree">Programme visée</label>
        <MultiSelect
          id="programme"
          options={programmes}
          placeholder="Choisir programme(s)..."
          bind:value={programmeSelected}
        >
        </MultiSelect>
      </div>      
      <div class="form-group-horizontal">
        <label for="conciliation">Conciliation</label>
        <input type="checkbox" bind:checked={offre.conciliation} class="form-control" id="conciliation" />
      </div>
      <div class="form-group-horizontal">
        <label for="urgente">Urgente</label>
        <input type="checkbox" bind:checked={offre.urgente} class="form-control" id="urgente" />
      </div>
      <div class="form-group-horizontal">
        <label for="lien">Lien</label>
      <Button text="Enregistrer" on:click={() => handleSubmit()} />
    </form>
    
  </div>
  