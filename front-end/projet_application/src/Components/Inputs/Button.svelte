<script lang="ts">
  export let text: string;
  export let submit: boolean = false;
</script>

{#if submit}
  <input type="submit" class="dropbtn" value={text} />
{:else}
  <button class="dropbtn">{text}</button>
{/if}

<style>
  /* Dropdown Button */
  .dropbtn {
    background-color: #233845;
    color: white;
    padding: 10px 15px;
    font-size: 16px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    cursor: pointer;
    transition: background-color 0.3s ease; /* Add a smooth transition */
  }

  /* Dropdown button on hover & focus */
  .dropbtn:hover,
  .dropbtn:focus {
    background-color: #4b9d93;
  }
</style>
