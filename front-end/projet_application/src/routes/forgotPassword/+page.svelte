<script lang="ts">
  import Button from "../../Components/Inputs/Button.svelte";
  import Link from "../../Components/Inputs/Link.svelte";
  import "../../styles/forgotPassword.css";
  import "../../styles/global.css";
  import type { Login } from "../../Models/Login";

  let error = "";

  let login: Login = {
    email: "",
    password: "",
  };
</script>

<section>
  <div class="forgotPassword">
    <h1>Mot de passe oublié</h1>
    <form class="forgotPassword-form" on:submit|preventDefault>
      <label for="email">Entrez votre courriel</label>
      <input
        type="text"
        class="input-forgotPassword"
        id="email"
        name="email"
        required
        bind:value={login.email}
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
