<script>
  import "../../styles/global.css";
  import "../../styles/register.css";
  let firstName = "";
  let lastName = "";
  let address = "";
  let city = "";
  let zipCode = "";
  let province = "";
  let email = "";
  let password = "";
  let validatePassword = "";

  import Button from "../../Components/Inputs/Button.svelte";

  function handleSubmit() {
    // Here you can handle form submission, for now, just logging the values
    console.log({
      firstName,
      lastName,
      address,
      city,
      zipCode,
      province,
      email,
      password,
      validatePassword,
    });
  }
</script>

<div class="container">
  <h1>Créer un compte</h1>

  <form on:submit|preventDefault={handleSubmit} class="form-register">
    <div class="form-inputs">
      <label for="firstName">Prénom</label>
      <input type="text" id="firstName" bind:value={firstName} required />
    </div>
    <div class="form-inputs">
      <label for="lastName">Nom de famille</label>
      <input type="text" id="lastName" bind:value={lastName} required />
    </div>
    <div class="form-inputs">
      <label for="address">Adresse</label>
      <input type="text" id="address" bind:value={address} required />
    </div>
    <div class="form-inputs">
      <label for="city">Ville</label>
      <input type="text" id="city" bind:value={city} required />
    </div>
    <div class="form-inputs">
      <label for="zipCode">Code Postal</label>
      <input type="text" id="zipCode" bind:value={zipCode} required />
    </div>
    <div class="form-inputs">
      <label for="province">Province</label>
      <input type="text" id="province" bind:value={province} required />
    </div>
    <div class="form-inputs">
      <label for="email">Courriel</label>
      <input type="email" id="email" bind:value={email} required />
    </div>
    <div class="form-inputs">
      <label for="password">Mot de passe</label>
      <input type="password" id="password" bind:value={password} required />
    </div>
    <div class="form-inputs">
      <label for="password">Valider Mot de passe</label>
      <input
        type="password"
        id="confirm_password"
        bind:value={validatePassword}
        required
      />
    </div>
    <div class="form-inputs form-buttons">
      <Button on:click text="Créer" />
    </div>
  </form>
</div>