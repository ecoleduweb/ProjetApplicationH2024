<script>
  import Button from "../../Components/Inputs/Button.svelte";
  import Link from "../../Components/Inputs/Link.svelte";
  import "../../styles/resetPassword.css";
  import "../../styles/global.css";

  let error = "";
</script>

<section>
  <div class="forgotPassword">
    <h1>Mot de passe oublié</h1>
    <form class="forgotPassword-form">
      <label for="username">Entrer un nouveau mot de passe </label>
      <input
        type="password"
        class="input-forgotPassword"
        id="password"
        name="password"
        required
      />
      <p class="text-title">Votre mot de passe doit contenir au minimum :</p>
      <ul class="list-requirements">
        <li><p class="text-password">12 caractères minimum</p></li>
        <li><p class="text-password">1 lettre majusucule</p></li>
        <li><p class="text-password">1 chiffre</p></li>
        <li><p class="text-password">1 caractère spéciaux</p></li>
      </ul>
      <label for="username">Confirmer le mot de passe </label>
      <input
        type="password"
        class="input-forgotPassword"
        id="confirmPassword"
        name="confirmPassword"
        required
      />
      {#if error}
        <p>{error}</p>
      {/if}
      <div class="buttons">
        <div class="button">
          <Button text="Confirmer" submit={true} />
        </div>
      </div>
    </form>
  </div>
</section>
