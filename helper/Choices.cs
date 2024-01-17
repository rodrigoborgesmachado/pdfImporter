using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace helper
{
    internal class Choices
    {
        public MessagesChat message { get; set; }
        public string logprobs { get; set; }
        public string finish_reason { get; set; }
        public int index { get; set; }
    }
}
