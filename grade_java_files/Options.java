package websheets;

public class Options { 

    // public instead of protected for similar reason to
    // http://stackoverflow.com/questions/3071720/
    public String title;
    public Boolean quietOnPass;
    public String stdin;
    public String stdinURL;
    public String saveAs;
    public Boolean expectException;
    public Boolean cloneForStudent;
    public Boolean cloneForReference;
    public Boolean ignoreTrailingSpaces;
    public Boolean ignoreRealFormatting;
    public Double realTolerance;
    public Integer maxOutputBytes;
    public Boolean dontRunReference;

    protected static Options defaultOptions;
    static Options nullOptions;
    static {
        nullOptions = new Options();
        defaultOptions = new Options();
        defaultOptions.quietOnPass = false;
        defaultOptions.expectException = false;
        defaultOptions.cloneForStudent = true;
        defaultOptions.cloneForReference = true;
        defaultOptions.ignoreTrailingSpaces = true;
        defaultOptions.ignoreRealFormatting = true;
        defaultOptions.realTolerance = 1E-4;
        defaultOptions.maxOutputBytes = 10000;
        defaultOptions.dontRunReference = false;
        // the remaining String fields have default value equal to null
    }

    void copyFrom(Options o, boolean overwriteNonNull) {
        if (overwriteNonNull || this.title == null) this.title = o.title;
        if (overwriteNonNull || this.quietOnPass == null) this.quietOnPass = o.quietOnPass;
        if (overwriteNonNull || this.stdin == null) this.stdin = o.stdin;
        if (overwriteNonNull || this.stdinURL == null) this.stdinURL = o.stdinURL;
        if (overwriteNonNull || this.saveAs == null) this.saveAs = o.saveAs;
        if (overwriteNonNull || this.expectException == null) this.expectException = o.expectException;
        if (overwriteNonNull || this.cloneForStudent == null) this.cloneForStudent = o.cloneForStudent;
        if (overwriteNonNull || this.cloneForReference == null) this.cloneForReference = o.cloneForReference;
        if (overwriteNonNull || this.ignoreTrailingSpaces == null) this.ignoreTrailingSpaces = o.ignoreTrailingSpaces;
        if (overwriteNonNull || this.ignoreRealFormatting == null) this.ignoreRealFormatting = o.ignoreRealFormatting;
        if (overwriteNonNull || this.realTolerance == null) this.realTolerance = o.realTolerance;
        if (overwriteNonNull || this.maxOutputBytes == null) this.maxOutputBytes = o.maxOutputBytes;
        if (overwriteNonNull || this.dontRunReference == null) this.dontRunReference = o.dontRunReference;
    }
    
    // replace any null field with value from defaultOptions
    void fillWithDefaults() { copyFrom(defaultOptions, false); }

    // set all options to null
    void clear() { copyFrom(nullOptions, true); }
}

