// See https://aka.ms/new-console-template for more information

using helper;
using Newtonsoft.Json;

string diretorio = "C:/provas/saida";
string arquivoPy = "pdfReader/concurso.py";
Directory.Delete(diretorio, true);
Directory.CreateDirectory(diretorio);

Console.WriteLine("Start Python.");
if (!Funcoes.Executa("py", arquivoPy))
{
    Console.WriteLine($"Erro ao rodar py {arquivoPy}.");
    return;
}
Console.WriteLine("Finshed Python.");

string fileOut = diretorio + "/json.json";
if (File.Exists(fileOut)) File.Delete(fileOut);

var files = Directory.GetFiles(diretorio);

List<string> gabarito = Funcoes.CarregaGabarito();
List<string> materias = Funcoes.CarregaMaterias();
List<Questoes> questoes = new List<Questoes>();

int codigoProva = 145;
Console.WriteLine("Start processing files.");
bool errors = false;

List<int> questoesAnuladas = new List<int>() { 9, 20, 41 };
List<String> letras = new List<string>() { "A) ", "B) ", "C) ", "D) ", "E) " };

string complemento = "";

foreach (var file in files)
{
    try
    {
        Console.WriteLine($"Processing file {file}");
        var text = File.ReadAllText(file);
        QuestaoFromFile questao = JsonConvert.DeserializeObject<QuestaoFromFile>(text);
        if(questao != null && int.TryParse(questao.numeroquestao, out var numeroQuestao))
        {
            if (questoesAnuladas.Contains(numeroQuestao) || numeroQuestao == 26)
                continue;

            Questoes questoes1 = new Questoes();

            questoes1.Ativo = "1";
            questoes1.CodigoProva = codigoProva;
            questoes1.ObservacaoQuestao = string.Empty;
            questoes1.NumeroQuestao = numeroQuestao;
            questoes1.Materia = materias[numeroQuestao-1].ToUpper();
            questoes1.CampoQuestao = numeroQuestao <= 10 ? complemento + questao.questao : questao.questao;
            questoes1.RespostasQuestoes = new List<RespostasQuestoes>();

            int i = 0;
            foreach (var item in questao.respostas)
            {
                var temp = new RespostasQuestoes();
                temp.CodigoQuestao = 0;
                temp.TextoResposta = (item.Contains(letras[i]) ? item : (letras[i] + item)).Replace("\t", " ").Replace("\n", "").Replace("<br><br>", "");

                if(temp.TextoResposta.StartsWith("A A") || temp.TextoResposta.StartsWith("B B") || temp.TextoResposta.StartsWith("C C") || temp.TextoResposta.StartsWith("D D") || temp.TextoResposta.StartsWith("E E"))
                {
                    temp.TextoResposta = temp.TextoResposta.Substring(3);
                }

                switch (gabarito[questoes1.NumeroQuestao - 1]) 
                {
                    case "A":
                        temp.Certa = i == 0 ? "1" : "2";
                        break; 
                    case "B":
                        temp.Certa = i == 1 ? "1" : "2";
                        break;
                    case "C":
                        temp.Certa = i == 2 ? "1" : "2";
                        break; 
                    case "D":
                        temp.Certa = i == 3 ? "1" : "2";
                        break; 
                    case "E":
                        temp.Certa = i == 4 ? "1" : "2";
                        break;
                }

                questoes1.RespostasQuestoes.Add(temp);
                i++;
            }
            questoes.Add(questoes1);
        }
    }
    catch(Exception ex)
    {
        Console.WriteLine("Erro ao processar: " + ex.Message);
        errors = true;
    }
}

var texto = JsonConvert.SerializeObject(questoes);

File.WriteAllText(fileOut, texto.ToString());
Console.WriteLine($"Finished. {(errors ? "There were erorrs." : "No errors.")}");
