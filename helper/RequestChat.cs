using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace helper
{
    internal class RequestChat
    {
        public string model { get; set; }
        public List<MessagesChat> messages { get; set; }
        public decimal temperature { get; set; }
    }
}
