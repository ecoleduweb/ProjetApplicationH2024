<script>
  import Button from "../../Components/Inputs/Button.svelte";
  import Link from "../../Components/Inputs/Link.svelte";
  import "../../styles/forgotPassword.css";
  import "../../styles/global.css";

  let error = "";
</script>

<section>
  <div class="forgotPassword">
    <h1>Mot de passe oublié</h1>
    <form class="forgotPassword-form">
      <label for="username">Entrez votre courriel</label>
      <input
        type="text"
        class="input-forgotPassword"
        id="username"
        name="username"
        required
      />
      <p class="text-password">
        Un courriel vous sera envoyé pour réinitialiser votre mot de passe
      </p>
      {#if error}
        <p>{error}</p>
      {/if}
      <div class="buttons">
        <div class="button">
          <Link text="Retour" href="/login" />
        </div>
        <div class="button">
          <Button text="Confirmer" submit={true} />
        </div>
      </div>
    </form>
  </div>
</section>
