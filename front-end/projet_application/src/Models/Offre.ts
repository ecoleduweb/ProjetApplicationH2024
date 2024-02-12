

export interface Offre { 
    titre: string; // titre de l'offre
    employeur: string; // nom de l'employeur
    active: boolean; // si l'offre est active ou non

    // periode de travail du stage
    periodeJour: boolean; 
    periodeSoir: boolean;
    periodeNuit: boolean;
    periodeFinDeSemaine: boolean;
    
    // saison de travail du stage
    saisonHiver: boolean;
    saisonEte: boolean; 
    saisonAutomne: boolean;
    saisonPrintemps: boolean;

    heure: string; // heure par semaine
    salaire: string; // salaire de lheure 
    stage: boolean; // si stage vrai sinon faux
    duree: string; // temps partiel, temps plein
    programme: string; // le programme visée par l'offre
    conciliation: string; // employeur conciliant ou non
    urgente: boolean; // si l'offre est urgente
    lien: string; // lien vers l'offre ou site web de l'employeur
    description: string; // description de l'offre
    dateAffichageDebut: string; // date de début de l'affichage
    dateAffichageFin: string; // date de fin de l'affichage
    personneContact: string; // nom de la personne à contacter
    courrielContact: string; // courriel de la personne à contacter
    telephoneContact: string; // téléphone de la personne à contacter
} 