using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace helper
{
    internal class ChatResponse
    {
        public string id { get; set; }
        public string model { get; set; }
        public List<Choices> choices { get; set; }
    }
}
