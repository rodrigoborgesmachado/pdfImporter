using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http.Headers;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

namespace helper
{
    public static class Chat
    {
        public async static Task<string> GetQuestaoCorrigida(string texto)
        {
            string retorno = string.Empty;

            try
            {
                using (var httpClient = new HttpClient())
                {
                    using (var request = new HttpRequestMessage(new HttpMethod("POST"), "https://api.openai.com/v1/chat/completions"))
                    {
                        request.Headers.TryAddWithoutValidation("Authorization", "Bearer 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");


                        request.Content = new StringContent(CreateObject(texto));   
                        request.Content.Headers.ContentType = MediaTypeHeaderValue.Parse("application/json");

                        var response = await httpClient.SendAsync(request);
                        var message = await response.Content.ReadAsStringAsync();
                        ChatResponse chatResponse = JsonConvert.DeserializeObject<ChatResponse>(message);

                        if(chatResponse != null && chatResponse.choices != null && chatResponse.choices.Count >= 1) 
                        { 
                            retorno = chatResponse.choices.FirstOrDefault().message.content;
                        }
                        else
                        {

                        }
                    }
                }
            }
            catch {
                retorno = texto;
            }

            return retorno;
        }

        private static string CreateObject(string questao)
        {
            string retorno = string.Empty;

            MessagesChat messagesChat = new MessagesChat() 
            { 
                role = "user",
                content = $"Poderia por favor corrigir essa mensagem e manter o códigon html da mesma? \"{questao}\""
            };
            

            RequestChat requestChat = new RequestChat() 
            {
                model = "gpt-3.5-turbo",
                messages = new List<MessagesChat>() { messagesChat },
                temperature = 0.7M,
            };


            return JsonConvert.SerializeObject(requestChat);
        }
    }
}
