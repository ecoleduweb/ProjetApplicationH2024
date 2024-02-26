<script lang="ts">
  import "../../styles/global.css";
  import Button from "../../Components/Inputs/Button.svelte";
  import Link from "../../Components/Inputs/Link.svelte";
  import type { Register } from "../../Models/Register.ts";

  let register: Register = {
    user: {
      id: 0,
      firstName: "",
      lastName: "",
      email: "",
      password: "",
      role: "",
    },
    nameEnterprise: "",
    address: "",
    city: "",
    phone: "",
    zipCode: "",
    province: "",
    validatePassword: "",
  };

  function handleSubmit() {
    // Here you can handle form submission, for now, just logging the values
    console.log(register);
  }
</script>

<div class="container">
  <h1>Créer un compte</h1>

  <form on:submit|preventDefault={handleSubmit} class="form-register">
    <div class="info-block">
      <h2>Informations personnelles</h2>
      <div class="form-fields">
        <div class="form-inputs">
          <label for="firstName">Prénom</label>
          <input
            type="text"
            id="firstName"
            bind:value={register.user.firstName}
            required
          />
        </div>
        <div class="form-inputs">
          <label for="lastName">Nom de famille</label>
          <input
            type="text"
            id="lastName"
            bind:value={register.user.lastName}
            required
          />
        </div>
      </div>
    </div>
    <div class="info-block">
      <h2>Informations de l'entreprise</h2>
      <div class="form-fields">
        <div class="form-inputs">
          <label for="entreprise">Nom Entreprise</label>
          <input
            type="text"
            id="entreprise"
            bind:value={register.nameEnterprise}
            required
          />
        </div>
        <div class="form-inputs">
          <label for="address">Adresse</label>
          <input
            type="text"
            id="address"
            bind:value={register.address}
            required
          />
        </div>
        <div class="form-inputs">
          <label for="city">Ville</label>
          <input type="text" id="city" bind:value={register.city} required />
        </div>
        <div class="form-inputs">
          <label for="zipCode">Code Postal</label>
          <input
            type="text"
            id="zipCode"
            bind:value={register.zipCode}
            required
          />
        </div>
        <div class="form-inputs">
          <label for="province">Province</label>
          <input
            type="text"
            id="province"
            bind:value={register.province}
            required
          />
        </div>
      </div>
    </div>
    <div class="info-block">
      <h2>Informations de l'utilisateur</h2>
      <div class="form-connexion">
        <div class="form-inputs">
          <label for="email">Courriel</label>
          <input
            type="email"
            id="email"
            bind:value={register.user.email}
            required
          />
        </div>
        <div class="form-inputs">
          <label for="password">Mot de passe</label>
          <input
            type="password"
            id="password"
            bind:value={register.user.password}
            required
          />
        </div>
        <div class="form-inputs">
          <label for="password">Valider Mot de passe</label>
          <input
            type="password"
            id="confirm_password"
            bind:value={register.validatePassword}
            required
          />
        </div>
      </div>
    </div>
    <div class="form-inputs form-submit">
      <div class="form-buttons">
        <Link text="Retour" href="/" />
      </div>
      <div class="form-buttons">
        <Button submit={true} text="Créer" />
      </div>
    </div>
  </form>
</div>

<style scoped>
  @import "../../styles/register.css";
</style>
