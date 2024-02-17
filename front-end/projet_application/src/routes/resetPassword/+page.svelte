<script lang="ts">
  import Button from "../../Components/Inputs/Button.svelte";
  import "../../styles/resetPassword.css";
  import "../../styles/global.css";
  import type { ResetPassword } from "../../Models/ResetPassword.ts";
  import type { ErrorResponse } from "../../Models/ErrorResponse.ts";
  import * as yup from "yup";

  const schema = yup.object().shape({
    password: yup.string().required("Entrer un mot de passe"),
    confirmPassword: yup.string().required("Saisir le mot de passe à nouveau"),
  });

  let errors: ResetPassword = {
    password: "",
    confirmPassword: "",
  };

  let resetPassword: ResetPassword = {
    password: "",
    confirmPassword: "",
  };

  const handleSubmit = async () => {
    try {
      // `abortEarly: false` to get all the errors
      await schema.validate(resetPassword, { abortEarly: false });
      errors = {
        password: "",
        confirmPassword: "",
      };

      console.log(resetPassword);
    } catch (err) {
      errors = extractErrors(err);
    }
  };
  function extractErrors(err: ErrorResponse | any) {
    return err.inner.reduce((acc: string[], err: ErrorResponse) => {
      return { ...acc, [err.path]: err.message };
    }, {});
  }
</script>

<section>
  <div class="forgotPassword">
    <h1>Mot de passe oublié</h1>
    <form class="forgotPassword-form" on:submit|preventDefault={handleSubmit}>
      <label for="email">Entrer un nouveau mot de passe </label>
      <input
        type="password"
        class="input-forgotPassword"
        id="password"
        name="password"
        bind:value={resetPassword.password}
      />
      <p class="errors-input">
        {#if errors.password}{errors.password}{/if}
      </p>
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
        bind:value={resetPassword.confirmPassword}
      />
      <p class="errors-input">
        {#if errors.confirmPassword}{errors.confirmPassword}{/if}
      </p>
      <div class="buttons">
        <div class="button">
          <Button text="Confirmer" submit={true} />
        </div>
      </div>
    </form>
  </div>
</section>
