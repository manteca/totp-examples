class Tarea1Controller < ApplicationController
  def index

    label = "FV Example"
    mail = "fvillalobos@medioclick.com"
    #TODO: Con la Herramineta totp, se puede genera un secret aleatoriio, pero se deja fijo para realizar pruebas.
    secret = "JBSWY3DPEHPK3PXP"
    issuer = "FV Example"
    chl = "otpauth://totp/#{label}:#{mail}?secret=#{secret}&issuer=#{issuer}"

    @secret = chl
    @var_url = "https://chart.googleapis.com/chart?chs=200x200&chld=M|0&cht=qr&chl="+ ERB::Util.u(chl) 

    totp = ROTP::TOTP.new(secret, issuer: issuer)

    @result = ""
    if params[:code] != nil
      #DEBUG: No debe pasar a produccion
      logger.info "PASE"
      logger.info totp.now
      logger.info "Verificaion Manual:" + totp.verify(totp.now).to_s()
      logger.info "Tiempo:" + Time.now.to_s()
      logger.info "URL:" + totp.provisioning_uri(mail).to_s()


      if totp.verify_with_drift(params[:code], 60)
        @result = "Correcto"
      else
        @result = "Incorrecto"
      end
    else
      @result = "ERROR: REVISAR CODIGO"
    end


  end


end
