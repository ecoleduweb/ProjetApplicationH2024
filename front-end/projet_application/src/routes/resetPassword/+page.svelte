<script lang="ts">
  import Button from "../../Components/Inputs/Button.svelte";
  import "../../styles/resetPassword.css";
  import "../../styles/global.css";
  import type { ResetPassword } from "../../Models/ResetPassword.ts";
  let error = "";

  let resetPassword: ResetPassword = {
    password: "",
    confirmPassword: "",
  };
</script>

<section>
  <div class="forgotPassword">
    <h1>Mot de passe oublié</h1>
    <form class="forgotPassword-form" on:submit|preventDefault>
      <label for="email">Entrer un nouveau mot de passe </label>
      <input
        type="password"
        class="input-forgotPassword"
        id="password"
        name="password"
        required
        bind:value={resetPassword.password}
      />
      <p class="text-title">Votre mot de passe doit contenir au minimum :</p>
      <ul class="list-requirements">
        <li><p class="text-password">12 caractères minimum</p></li>
        <li><p class="text-password">1 lettre majusucule</p></li>
        <li><p class="text-password">1 chiffre</p></li>
        <li><p class="text-password">1 caractère spéciaux</p></li>
      </ul>
      <label for="email">Confirmer le mot de passe </label>
      <input
        type="password"
        class="input-forgotPassword"
        id="confirmPassword"
        name="confirmPassword"
        required
        bind:value={resetPassword.confirmPassword}
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
