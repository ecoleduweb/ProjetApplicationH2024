<script lang="ts">
    import Modal from "../Common/Modal.svelte";
    import type { Emploi } from "../../Models/Emploi";
    export let emploi: Emploi;
    export let handleEmploiClick: () => void;
</script>

<Modal handleModalClick={handleEmploiClick}>
    <div class="container">
        <div class="info">
            <p class="text">{emploi.titre}</p>
            <p class="text">{emploi.entreprise}</p>
            <p class="text">{emploi.dateFin}</p>
            <p class="text">{emploi.description}</p>
        </div>
    </div>
</Modal>

<style>
    .info {
        font-size: 1.3rem;
        margin-bottom: 20px;
        color: black;
    }
    .text {
        margin-right: 10px;
    }
    .container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
</style>
