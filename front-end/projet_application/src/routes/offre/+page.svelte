<script lang="ts">
    import "../../styles/global.css";
    import "../../styles/offre.css";
    import Button from "../../Components/Inputs/Button.svelte";
    import MultiSelect from 'svelte-multiselect';
    import type { Offre } from "../../Models/Offre";
    import { POST } from "../../ts/server";
    import * as yup from "yup";
    import { extractErrors } from "../../ts/utils";
  
    const schema = yup.object().shape({
    titre: yup.string().required("Le titre du poste est requis"),
    lieu: yup.string().required("Le lieu de travail est requis"),
    description: yup.string().required("La description de l'offre est requise"),
    dateEntreeFonction: yup.string().required("La date d'entrée en fonction est requise").test('is-date', "Veuillez choisir une date valide !", value => {
    return !isNaN(Date.parse(value));
    }),
    dateLimitePostuler: yup.string().required("La date d'entrée en fonction est requise").test('is-date', "Veuillez choisir une date valide !", value => {
    return !isNaN(Date.parse(value));
    }),
    salaire: yup.string().required("Le salaire est requis").matches(/^\d*(\.\d+)?$/,
     "Le salaire doit être un nombre ou un nombre à unité (20.50)").min(0, "Le salaire doit être positif"),
    courrielContact: yup.string().email("Le courriel de contact n'est pas valide").required("Le courriel de contact est requis"),
    typeEmplois: yup.string().required("Le type d'emplois est requis"),
    programme: yup.string().required("Le programme visé est requis"),
    
  });

    let offre: Offre = {
    titre: "",
    lieu: "",
    dateEntreeFonction: "",
    dateLimitePostuler: "",
    salaire: 0,
    typeEmplois: "",
    heures: 0,
    programme: "",
    conciliation: false, 
    urgente: false,
    lien: "",
    description: "",
    courrielContact: "",
    active: true,
    };

    let errors: Offre = {
    titre: "",
    lieu: "",
    dateEntreeFonction: "",
    dateLimitePostuler: "",
    salaire: 0,
    typeEmplois: "",
    heures: 0,
    programme: "",
    conciliation: false, 
    urgente: false,
    lien: "",
    description: "",
    courrielContact: "",
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



  const handleSubmit = async () => {
    console.log(offre);
    console.log(programmeSelected);
    console.log(typeEmploisSelected);
    // take all content from programSelected and put it in offre.programme
    offre.typeEmplois = typeEmploisSelected.map((typeEmploi) => typeEmploi.label).join(", ");
    try {
      // `abortEarly: false` to get all the errors
      await schema.validate(offre, { abortEarly: false });
      errors = {
        titre: "",
        lieu: "",
        dateEntreeFonction: "",
        dateLimitePostuler: "",
        salaire: 0,
        typeEmplois: "",
        heures: 0,
        programme: "",
        conciliation: false, 
        urgente: false,
        lien: "",
        description: "",
        courrielContact: "",
        active: true,
      };

      console.log(offre);
      const response = POST("/auth/login", offre); // PATH DE L'AJOUT DE L'OFFRE A MODIFIER
      console.log(response);
    } catch (err) {
      errors = extractErrors(err);
    }
  };

  </script>
  
  <div class="container">
    <form on:submit|preventDefault={handleSubmit} class="form-offre">
      <h1>Créer une nouvelle offre d'emploi</h1>
      <div class="form-group-vertical">
        <label for="titre">Titre du poste*</label>
        <input type="text" bind:value={offre.titre} class="form-control" id="titre" />
      </div>
      <p class="errors-input">
        {#if errors.titre}{errors.titre}{/if}
      </p>
      <div class="form-group-vertical">
        <label for="typeEmplois">Type d'emplois*</label>
        <MultiSelect
          id="periode"
          options={typeEmplois}
          placeholder="Choisir période(s)..."
          bind:value={typeEmploisSelected}
        />
      </div>
      <p class="errors-input">
        {#if errors.typeEmplois}{errors.typeEmplois}{/if}
      </p>
      <div class="form-group-vertical">
        <label for="lieu">Lieu de travail*</label>
        <input type="text" bind:value={offre.lieu} class="form-control" id="salaire" />
      </div>
      <p class="errors-input">
        {#if errors.lieu}{errors.lieu}{/if}
      </p>
      <div class="form-group-vertical">
        <label for="dateEntree">Date d'entrée en fonction</label>
        <input type="date" bind:value={offre.dateEntreeFonction} class="form-control" id="dateEntree" />
      </div>
      <p class="errors-input">
        {#if errors.dateEntreeFonction}{errors.dateEntreeFonction}{/if}
      </p>
      <div class="form-group-vertical">
        <label for="dateLimite">Date limite pour postuler</label>
        <input type="date" bind:value={offre.dateLimitePostuler} class="form-control" id="dateLimite" />
      </div>
      <p class="errors-input">
        {#if errors.dateLimitePostuler}{errors.dateLimitePostuler}{/if}
      </p>
      <div class="form-group-vertical">
        <label for="duree">Programme visée</label>
        <MultiSelect
          id="programme"
          options={programmes}
          placeholder="Choisir programme(s)..."
          bind:value={programmeSelected}
        >
        </MultiSelect>
      </div> 
      <p class="errors-input">
        {#if errors.programme}{errors.programme}{/if}
      </p>
      <div class="form-group-vertical">
        <label for="salaire">Salaire (Heure)*</label>
        <input type="text" bind:value={offre.salaire} class="form-control" id="salaire" />
      </div>
      <p class="errors-input">
          {#if errors.salaire}{errors.salaire}{/if}
      </p>
      <div class="form-group-vertical">
        <label for="heure">Heure (Semaine)*</label>
        <input type="text" bind:value={offre.heures} class="form-control" id="heure" />
      </div>
      <p class="errors-input">
          {#if errors.salaire}{errors.salaire}{/if}
      </p>
      <div class="form-group-horizontal">
        <label for="conciliation">Conciliation</label>
        <input type="checkbox" bind:checked={offre.conciliation} class="form-control" id="conciliation" />
      </div>
      <div class="form-group-horizontal">
        <label for="urgente">Urgente</label>
        <input type="checkbox" bind:checked={offre.urgente} class="form-control" id="urgente" />
      </div>
      <div class="form-group-vertical">
        <label for="lien">Lien</label>
        <input type="text" bind:value={offre.lien} class="form-control" id="lien" />
      </div>
      <div class="form-group-vertical">
        <label for="courriel-contact">Courriel contact</label>
        <input type="text" bind:value={offre.courrielContact} class="form-control" id="courriel-contact" />
      </div>
      <div class="form-group-vertical">
        <label for="description">Description du poste*</label>
        <textarea rows="15" cols="50" bind:value={offre.description} class="form-control" id="description" />
      </div>
      <Button submit={true} text="Enregistrer" on:click={() => handleSubmit()} />
    </form>
  </div>