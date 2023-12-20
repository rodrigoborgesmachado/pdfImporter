namespace helper
{
    public class Questoes
    {
        public DateTime DataRegistro { get; set; }

        public string CampoQuestao { get; set; }

        public string ObservacaoQuestao { get; set; }

        public string Materia { get; set; }

        public int CodigoProva { get; set; }

        public int NumeroQuestao { get; set; }

        public string Ativo { get; set; }

        public DateTime UpdatedOn { get; set; }

        public int UpdatedBy { get; set; }

        public int CreatedBy { get; set; }

        public List<RespostasQuestoes> RespostasQuestoes { get; set; }
    }
}
