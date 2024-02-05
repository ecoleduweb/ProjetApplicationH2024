<script>
  import "../../styles/global.css";
  let firstName = "";
  let lastName = "";
  let address = "";
  let city = "";
  let zipCode = "";
  let province = "";
  let email = "";
  let password = "";
  let validatePassword = "";

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

<h1>Créer un compte</h1>

<form on:submit|preventDefault={handleSubmit}>
  <label for="firstName">Prénom</label>
  <input type="text" id="firstName" bind:value={firstName} required />

  <label for="lastName">Nom de famille</label>
  <input type="text" id="lastName" bind:value={lastName} required />

  <label for="address">Adresse</label>
  <input type="text" id="address" bind:value={address} required />

  <label for="city">Ville</label>
  <input type="text" id="city" bind:value={city} required />

  <label for="zipCode">Code Postal</label>
  <input type="text" id="zipCode" bind:value={zipCode} required />

  <label for="province">Province</label>
  <input type="text" id="province" bind:value={province} required />

  <label for="email">Courriel</label>
  <input type="email" id="email" bind:value={email} required />

  <label for="password">Mot de passe</label>
  <input type="password" id="password" bind:value={password} required />

  <label for="password">Valider Mot de passe</label>
  <input
    type="password"
    id="confirm_password"
    bind:value={validatePassword}
    required
  />
  <button type="submit">Register</button>
</form>

<style>
  /* Some basic styles for demonstration */
  label {
    display: block;
    margin-bottom: 5px;
  }

  input {
    margin-bottom: 10px;
  }

  button {
    margin-top: 10px;
  }
</style>
