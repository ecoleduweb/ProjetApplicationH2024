<script lang="ts">
  import Button from "../../Components/Inputs/Button.svelte";
  import Link from "../../Components/Inputs/Link.svelte";
  import "../../styles/login.css";
  import "../../styles/global.css";
  import type { Login } from "../../Models/Login";
  import { POST } from "../../ts/server";

  let error = "";
  let form: Login = {
    email: "",
    password: "",
  };

  const handleSubmit = async () => {
    console.log(form);
    const response = POST("http://localhost:5000/login", form);
    console.log(response);
  };
</script>

<section>
  <div class="login">
    <h1>Authentification</h1>
    <form on:submit|preventDefault={handleSubmit} class="login-form">
      <label for="email">Nom d'utiliasteur</label>
      <input
        type="text"
        class="input-login"
        id="email"
        name="email"
        required
        bind:value={form.email}
      />
      <label for="password">Mot de passe</label>
      <input
        type="password"
        class="input-login"
        id="password"
        name="password"
        required
        bind:value={form.password}
      />
      {#if error}
        <p>{error}</p>
      {/if}
      <Button text="Se connecter" submit={true} />
      <div class="submit">
        <Link href="forgotPassword" text="Mot de passe oublié ?" />
      </div>
      <Link href="register" text="Créer un utilisateur" />
    </form>
  </div>
</section>
