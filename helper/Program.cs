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

int codigoProva = 143;
Console.WriteLine("Start processing files.");
bool errors = false;

List<int> questoesAnuladas = new List<int>() { 17, 21, 34 };
List<String> letras = new List<string>() { "A) ", "B) ", "C) ", "D) ", "E) " };

string complemento = "<center><b>O que as artes agregam ao debate sobre educação e inovação produtiva</b></center><br><br>A relação positiva entre arte e excelência na educação está amplamente comprovada por estudos como o de James Catterall (1948-2017), professor da Universidade da Califórnia (UCLA), que dedicou boa parte da sua vida para analisar pesquisas que provam como as artes desenvolvem a cognição do indivíduo, habilidade aplicável .... qualquer outra área do conhecimento.<br> Ana Mae Barbosa, uma das maiores especialistas brasileiras no tema, em artigo publicado em 2018, mostrou que a introdução das artes nos Ensinos Fundamental e Médio nos Estados Unidos, no programa conhecido como Stem (Science, Technology, Engineering and Mathematics), melhorou significativamente o fraco desempenho em ciências dos estudantes norte-americanos.<br> Por que menciono isso em meio .... uma tempestade provocada pela pandemia que deixou mais de 5,5 milhões de crianças e jovens brasileiros sem aulas em 2020 e, segundo estudo recente, divulgado pelo Todos pela Educação, 244 mil crianças e jovens entre 6-14 anos sem o direito .... educação?<br> Primeiro, o modelo fordista de escola precisa mudar. A pandemia acelerou um debate que se arrasta há anos, _____ da necessidade de olharmos para um sistema de ensinoaprendizagem que não responde mais ao tempo em que vivemos, e que faz as crianças e jovens de hoje, como seus pais, avós e bisavós, irem aos bancos escolares com pouca ou nenhuma motivação para enfrentarem o dia de estudos.<br> Além do modelo híbrido, é preciso aprofundar o que queremos das escolas; qual ambiente físico melhor acolhe e estimula em uma era de uso exacerbado das tecnologias; se as didáticas e práticas que discutimos incentivam a cooperação, a criatividade e a resolução de problemas; ou se ainda estamos presos em um sistema que contribui para a evasão e o desinteresse. Como a cultura pode contribuir para a mudança? E como pode cooperar com o desenvolvimento de jovens mais preparados?<br> Primeiro, arte e cultura são ferramentas de extrema importância para o conhecimento e a educação de qualidade. Segundo, a produtividade do país depende de formação continuada, e o motor econômico no século 21 é a economia do conhecimento, impulsionada pelo investimento em inovação e, no ensino das ciências básicas, pelo acesso e pelo desenvolvimento das tecnologias e pelos setores das artes, do design, da gastronomia, da moda, do entretenimento e de todo o conjunto das chamadas indústrias criativas.<br> No meio das várias crises que temos vivenciado, ___ algumas oportunidades que podemos aproveitar. Contudo, para algo acontecer é preciso um plano orientado de trabalho – pedagógico, mas também de governança – e o engajamento do sistema cultural, que enfrenta dificuldades combinadas, mas apresenta resiliência e uma boa rede básica de gestão. Entretanto, abrir um diálogo com as secretarias de educação e organizar uma oferta a partir da sua rede de programas e instituições, é algo que pode ser feito de imediato. Uma saída complementar é envolver fundações e institutos de educação e cultura que reúnam especialistas das áreas para elaborar as bases de um Plano de Arte e Cultura. Uma bússola inicial que oriente os _______ para um processo de implantação.<br> O importante é começar.<br><sub>(Disponível em: https://exame.com/blog/cultura-e-sociedade/ – texto adaptado especialmente para esta prova).</sub><br><br>";

foreach (var file in files)
{
    try
    {
        Console.WriteLine($"Processing file {file}");
        var text = File.ReadAllText(file);
        QuestaoFromFile questao = JsonConvert.DeserializeObject<QuestaoFromFile>(text);
        if(questao != null && int.TryParse(questao.numeroquestao, out var numeroQuestao))
        {
            if (questoesAnuladas.Contains(numeroQuestao) || numeroQuestao != 26)
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
