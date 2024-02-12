<script lang="ts">
  import Button from "../../Components/Inputs/Button.svelte";
  import Link from "../../Components/Inputs/Link.svelte";
  import "../../styles/login.css";
  import "../../styles/global.css";

  interface Login {
    username: string;
    password: string;
  }

  let error = "";
  let form: Login = {
    username: "",
    password: "",
  };
  const handleSubmit = async () => {
    console.log(form);

    const response = await fetch("http://localhost:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(form),
    });

    if (response.ok) {
      const data = await response.json();
      localStorage.setItem("token", data.token);
      location.href = "/";
    } else {
      error = await response.json();
      console.log(error);
    }
  };
</script>

<section>
  <div class="login">
    <h1>Authentification</h1>
    <form on:submit|preventDefault={handleSubmit} class="login-form">
      <label for="username">Nom d'utiliasteur</label>
      <input
        type="text"
        class="input-login"
        id="username"
        name="username"
        required
        bind:value={form.username}
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
